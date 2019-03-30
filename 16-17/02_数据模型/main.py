#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.view import View

def main():
    """主函数"""
    is_exit = False
    while not is_exit:
        try:
            View.menu()
        except KeyboardInterrupt:
            print('退出')
            is_exit = True
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    main()