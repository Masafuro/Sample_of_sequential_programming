from multiprocessing.managers import BaseManager

class GlobalState:
    """
    唯一のグローバル状態。
    構造: {publisher: {key: {"value": any, "flag": bool}}}
    """
    def __init__(self):
        self.data = {}

    def get_all_data(self):
        """共有メモリから全データを取得する（モニター用）"""
        return self.data

    def update(self, publisher, key, value, flag):
        """
        値とフラグをセットで更新する。
        """
        if publisher not in self.data:
            self.data[publisher] = {}
        
        self.data[publisher][key] = {
            "value": value,
            "flag": flag
        }

    def get_entry(self, publisher, key):
        """
        指定されたエントリを取得する。存在しない場合はデフォルト値を返す。
        """
        return self.data.get(publisher, {}).get(key, {"value": None, "flag": False})

# 実体化とマネージャー登録
state = GlobalState()

class StateManager(BaseManager):
    pass

StateManager.register('get_state', callable=lambda: state)