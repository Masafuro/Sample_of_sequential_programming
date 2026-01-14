import hashlib
from state import state

def compute_hash():
    # ユーザーからの入力を確認します
    request = state.get_entry('user', 'hash_request')
    
    if request['flag']:
        # ソルトを取得しますが、値が None であればスクリプト内のデフォルト値を使用します
        salt_entry = state.get_entry('security', 'salt')
        salt = salt_entry['value'] if salt_entry['value'] is not None else "local_default_salt"
        
        # 取得したソルトを用いてハッシュを計算します
        source_text = str(request['value']) + salt
        hashed_val = hashlib.sha256(source_text.encode()).hexdigest()
        
        # 結果をシステム領域に書き込み、フラグを立てます
        state.update('system', 'hash_result', hashed_val, True)
        
        print(f"\n[Hasher] HASH:{hashed_val}, salt: '{salt}')")
        
        # ユーザーのリクエストフラグを回収します
        state.update('user', 'hash_request', request['value'], False)