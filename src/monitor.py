import time
import copy
from datetime import datetime
from state import StateManager

def start_monitor():
    """
    共有メモリを監視し、変化があったエントリのみを一行で出力する。
    """
    manager = StateManager(address=('127.0.0.1', 50000), authkey=b'sequential')
    
    try:
        manager.connect()
    except ConnectionRefusedError:
        print("エラー: メインプロセスに接続できませんでした。")
        return

    remote_state = manager.get_state()
    
    # 個別の (publisher, key) の状態を保持する辞書
    # 構造: {(pub, key): {"value": v, "flag": f}}
    history = {}

    # ヘッダーの表示（Valueはハッシュ値が入るため長めに確保）
    header = f"{'TIMESTAMP':<12} | {'PUBLISHER':<10} | {'KEY':<15} | {'VALUE':<64} | {'FLAG':<5}"
    print(header)
    print("-" * len(header))

    try:
        while True:
            # 共有メモリから現在の全データを取得
            current_data = copy.deepcopy(remote_state.get_all_data())

            # 階層構造を走査
            for pub, keys in current_data.items():
                for key, entry in keys.items():
                    state_id = (pub, key)
                    
                    # 以前の記録がない、もしくは値かフラグに変化があった場合のみ出力
                    if state_id not in history or history[state_id] != entry:
                        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                        v = str(entry['value'])
                        f = "TRUE" if entry['flag'] else "false"
                        
                        # 指定された順序で一行出力
                        print(f"{timestamp:<12} | {pub:<10} | {key:<15} | {v:<64} | {f:<5}")
                        
                        # 履歴を更新
                        history[state_id] = entry
            
            # CPU負荷軽減のための待機
            time.sleep(0.01)
            
    except (EOFError, ConnectionResetError):
        print("\nメインプロセスが終了しました。")
    except KeyboardInterrupt:
        print("\n監視を停止しました。")

if __name__ == "__main__":
    start_monitor()