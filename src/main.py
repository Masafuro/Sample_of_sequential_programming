from state import state, StateManager
from controller import controller
from scripts.ui_input import wait_for_input
from scripts.hasher import compute_hash # 新規追加
import threading

# 初期状態のセットアップ
state.update('security', 'salt', 'initial_salt', False)

def start_memory_server():
    manager = StateManager(address=('127.0.0.1', 50000), authkey=b'sequential')
    manager.get_server().serve_forever()

threading.Thread(target=start_memory_server, daemon=True).start()

# ループの構築
controller.add(wait_for_input)
controller.add(compute_hash)

if __name__ == "__main__":
    controller.run()