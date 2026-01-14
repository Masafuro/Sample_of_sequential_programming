from state import StateManager
import sys

def start_salt_manager():
    manager = StateManager(address=('127.0.0.1', 50000), authkey=b'sequential')
    try:
        manager.connect()
    except:
        print("メインプロセスが見つかりません。")
        return

    remote_state = manager.get_state()
    print("--- SALT MANAGER ---")
    
    while True:
        new_salt = input("\n新しいソルト値を入力してください (exitで終了): ")
        if new_salt == "exit": break
        
        # メインプロセスが止まっていても、強制的にメモリを書き換える
        remote_state.update('security', 'salt', new_salt, True)
        print(f"ソルトを '{new_salt}' に更新しました。")

if __name__ == "__main__":
    start_salt_manager()