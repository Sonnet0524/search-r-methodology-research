#!/usr/bin/env python3
"""
Git安全管理工具

确保所有提交和推送都经过敏感信息审查。
"""

import os
import re
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Tuple

# 颜色输出
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_error(msg: str):
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")

def print_success(msg: str):
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")

# 敏感信息模式
SENSITIVE_PATTERNS = [
    # API Keys (排除示例值)
    (r'[Aa][Pp][Ii][_\-]?[Kk][Ee][Yy]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example)[\w\-]{20,}["\']?', "API Key"),
    (r'[Bb][Aa][Ii][Dd][Uu]_?[Aa][Pp][Ii]?_?[Kk][Ee][Yy]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example)[\w\-\/]{20,}["\']?', "Baidu API Key"),
    
    # Tokens (排除示例值)
    (r'[Tt][Oo][Kk][Ee][Nn]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example|<)[\w\-]{20,}["\']?', "Token"),
    (r'[Pp][Aa][Dd][Dd][Ll][Ee][Oo][Cc][Rr]_?[Aa][Cc][Cc][Ee][Ss][Ss]_?[Tt][Oo][Kk][Ee][Nn]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example|<)[\w\-]{20,}["\']?', "PaddleOCR Token"),
    (r'bce-v3/ALTAK-[a-zA-Z0-9]{20,}', "BCE Token"),
    
    # Passwords (排除示例值)
    (r'[Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example|<).{8,}["\']?', "Password"),
    
    # Secret Keys (排除示例值)
    (r'[Ss][Ee][Cc][Rr][Ee][Tt][_\-]?[Kk][Ee][Yy]\s*[=:]\s*["\']?(?!your_|xxx|placeholder|example)[\w\-]{20,}["\']?', "Secret Key"),
    
    # 用户专属URL (排除公共URL)
    (r'https?://[a-z0-9]{10,}\.(aistudio-app)\.com/[a-z\-]+', "用户专属URL"),
    
    # Bearer Token (排除示例值)
    (r'Bearer\s+(?!your_|xxx|placeholder|example|<)[\w\-\.]{20,}', "Bearer Token"),
]

# 禁止提交的文件模式
FORBIDDEN_FILES = [
    r'\.env$',
    r'\.env\.',
    r'\.env\.local',
    r'credentials',
    r'secrets',
    r'\.pem$',
    r'\.key$',
    r'id_rsa',
]


def scan_file_for_secrets(file_path: str) -> List[Dict]:
    """扫描文件中的敏感信息"""
    findings = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        for line_num, line in enumerate(lines, 1):
            for pattern, secret_type in SENSITIVE_PATTERNS:
                if re.search(pattern, line):
                    findings.append({
                        "file": file_path,
                        "line": line_num,
                        "type": secret_type,
                        "content": line.strip()[:100]  # 限制显示长度
                    })
    except Exception as e:
        pass  # 忽略无法读取的文件
    
    return findings


def check_gitignore() -> Tuple[bool, List[str]]:
    """检查.gitignore是否包含必要的忽略规则"""
    required_patterns = ['.env', '.env.local', '*.log']
    missing = []
    
    gitignore_path = '.gitignore'
    if not os.path.exists(gitignore_path):
        return False, required_patterns
    
    with open(gitignore_path, 'r') as f:
        content = f.read()
    
    for pattern in required_patterns:
        if pattern not in content:
            missing.append(pattern)
    
    return len(missing) == 0, missing


def is_forbidden_file(file_path: str) -> bool:
    """检查文件是否在禁止列表中"""
    file_name = os.path.basename(file_path)
    for pattern in FORBIDDEN_FILES:
        if re.search(pattern, file_path, re.IGNORECASE):
            return True
    return False


def get_staged_files() -> List[str]:
    """获取暂存区的文件列表"""
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only'],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.strip().split('\n') if f]


def get_untracked_files() -> List[str]:
    """获取未跟踪的文件列表"""
    result = subprocess.run(
        ['git', 'ls-files', '--others', '--exclude-standard'],
        capture_output=True,
        text=True
    )
    return [f for f in result.stdout.strip().split('\n') if f]


def check_sensitive_info(files: List[str]) -> Tuple[bool, List[Dict]]:
    """检查文件中的敏感信息"""
    all_findings = []
    
    for file_path in files:
        if is_forbidden_file(file_path):
            all_findings.append({
                "file": file_path,
                "line": 0,
                "type": "禁止提交的文件",
                "content": "该文件类型不应提交到仓库"
            })
        else:
            findings = scan_file_for_secrets(file_path)
            all_findings.extend(findings)
    
    return len(all_findings) == 0, all_findings


def cmd_check(args):
    """执行安全检查"""
    print_info("开始安全检查...")
    print()
    
    # 1. 检查.gitignore
    print_info("检查.gitignore...")
    gitignore_ok, missing = check_gitignore()
    if gitignore_ok:
        print_success(".gitignore检查通过")
    else:
        print_error(".gitignore缺少以下规则:")
        for pattern in missing:
            print(f"  - {pattern}")
    
    print()
    
    # 2. 获取要检查的文件
    if args.files:
        files = args.files
    else:
        files = get_staged_files() + get_untracked_files()
    
    if not files:
        print_info("没有待检查的文件")
        return True
    
    print_info(f"检查 {len(files)} 个文件...")
    print()
    
    # 3. 检查敏感信息
    safe, findings = check_sensitive_info(files)
    
    if safe:
        print_success("未发现敏感信息")
        return True
    else:
        print_error(f"发现 {len(findings)} 个敏感信息:")
        print()
        for f in findings:
            print(f"  文件: {f['file']}")
            if f['line'] > 0:
                print(f"  行号: {f['line']}")
            print(f"  类型: {f['type']}")
            print(f"  内容: {f['content'][:80]}...")
            print()
        return False


def cmd_commit(args):
    """执行安全提交"""
    print_info("准备提交...")
    print()
    
    # 1. 添加文件
    if args.files:
        print_info(f"添加文件到暂存区...")
        for file in args.files:
            subprocess.run(['git', 'add', file])
    else:
        print_info("添加所有更改到暂存区...")
        subprocess.run(['git', 'add', '-A'])
    
    # 2. 安全检查
    staged_files = get_staged_files()
    if not staged_files:
        print_warning("没有文件需要提交")
        return False
    
    print_info(f"检查 {len(staged_files)} 个暂存文件...")
    safe, findings = check_sensitive_info(staged_files)
    
    if not safe:
        print_error("安全检查失败！请处理以下问题:")
        print()
        for f in findings:
            print(f"  文件: {f['file']}")
            print(f"  类型: {f['type']}")
            print()
        
        # 取消暂存
        print_info("取消暂存...")
        subprocess.run(['git', 'reset', 'HEAD'])
        return False
    
    print_success("安全检查通过")
    print()
    
    # 3. 执行提交
    print_info(f"提交: {args.message}")
    result = subprocess.run(
        ['git', 'commit', '-m', args.message],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print_success("提交成功")
        print(result.stdout)
        return True
    else:
        print_error("提交失败")
        print(result.stderr)
        return False


def cmd_push(args):
    """执行安全推送"""
    print_info("准备推送...")
    print()
    
    # 1. 检查.gitignore
    print_info("步骤1: 检查.gitignore...")
    gitignore_ok, missing = check_gitignore()
    if not gitignore_ok:
        print_error(".gitignore缺少以下规则:")
        for pattern in missing:
            print(f"  - {pattern}")
        return False
    print_success(".gitignore检查通过")
    print()
    
    # 2. 检查待推送内容
    print_info("步骤2: 检查待推送内容...")
    
    # 获取待推送的提交
    branch = args.branch or 'main'
    result = subprocess.run(
        ['git', 'log', f'origin/{branch}..HEAD', '--oneline'],
        capture_output=True,
        text=True
    )
    
    commits = [line for line in result.stdout.strip().split('\n') if line]
    
    if not commits:
        print_info("没有待推送的提交")
        return True
    
    print_info(f"待推送提交数: {len(commits)}")
    for commit in commits:
        print(f"  {commit}")
    print()
    
    # 3. 扫描待推送的文件变更
    print_info("步骤3: 扫描文件变更...")
    result = subprocess.run(
        ['git', 'diff', f'origin/{branch}..HEAD', '--name-only'],
        capture_output=True,
        text=True
    )
    
    changed_files = [f for f in result.stdout.strip().split('\n') if f]
    
    if changed_files:
        print_info(f"变更文件数: {len(changed_files)}")
        
        safe, findings = check_sensitive_info(changed_files)
        
        if not safe:
            print_error("发现敏感信息！")
            print()
            for f in findings:
                print(f"  文件: {f['file']}")
                print(f"  类型: {f['type']}")
                print()
            return False
        
        print_success("敏感信息检查通过")
    print()
    
    # 4. 执行推送
    print_info("步骤4: 推送到远程仓库...")
    result = subprocess.run(
        ['git', 'push', 'origin', branch],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print_success("推送成功")
        print()
        
        # 5. 生成简报
        generate_report(commits, changed_files, branch)
        return True
    else:
        print_error("推送失败")
        print(result.stderr)
        return False


def generate_report(commits: List[str], changed_files: List[str], branch: str):
    """生成推送简报"""
    print("=" * 60)
    print("## Git 推送简报")
    print("=" * 60)
    print()
    print(f"**推送时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"**分支**: {branch}")
    print(f"**提交数量**: {len(commits)}")
    print()
    
    print("### 提交内容")
    for i, commit in enumerate(commits, 1):
        print(f"{i}. {commit}")
    print()
    
    print("### 安全检查")
    print("- ✅ .gitignore检查通过")
    print("- ✅ 敏感信息扫描通过")
    print("- ✅ 无禁止提交的文件")
    print()
    
    # 统计
    print("### 统计")
    print(f"- 变更文件: {len(changed_files)}")
    
    # 统计行数变更
    result = subprocess.run(
        ['git', 'diff', f'origin/{branch}~{len(commits)}..origin/{branch}', '--shortstat'],
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(f"- {result.stdout.strip()}")
    
    print()
    print("### 远程状态")
    print(f"- 远程仓库: origin/{branch}")
    print(f"- 推送状态: 成功")
    print()
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Git安全管理工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 检查当前状态
  python git_safe.py check
  
  # 提交更改
  python git_safe.py commit -m "提交说明"
  
  # 推送到远程
  python git_safe.py push
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # check命令
    check_parser = subparsers.add_parser('check', help='安全检查')
    check_parser.add_argument('--files', nargs='+', help='指定检查的文件')
    
    # commit命令
    commit_parser = subparsers.add_parser('commit', help='安全提交')
    commit_parser.add_argument('-m', '--message', required=True, help='提交说明')
    commit_parser.add_argument('--files', nargs='+', help='指定提交的文件')
    
    # push命令
    push_parser = subparsers.add_parser('push', help='安全推送')
    push_parser.add_argument('--branch', help='指定分支')
    
    args = parser.parse_args()
    
    if args.command == 'check':
        success = cmd_check(args)
        sys.exit(0 if success else 1)
    elif args.command == 'commit':
        success = cmd_commit(args)
        sys.exit(0 if success else 1)
    elif args.command == 'push':
        success = cmd_push(args)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
