import time

class SequentialController:
    def __init__(self):
        self.scripts = []
    
    def add(self, script):
        """実行するスクリプトを順番に追加します"""
        self.scripts.append(script)
    
    def run(self, interval=0.01):
        """登録された順序でスクリプトを永久に実行します"""
        while True:
            for script in self.scripts:
                script()
            time.sleep(interval)

# グローバルインスタンス
controller = SequentialController()