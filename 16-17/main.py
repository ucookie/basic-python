#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    """主函数"""
    is_exit = False
    while not is_exit:
        try:
            ToolsManager.menu()
        except KeyboardInterrupt:
            ControlView.notice(title='Exit deploy tools')
            is_exit = True
        except Exception, error:
            ControlView.notice_error(str(error))

if __name__ == '__main__':
    main()