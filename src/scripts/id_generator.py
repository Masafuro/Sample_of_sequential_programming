import random
import string
from state import state

def generate_id():
    # ユーザーからのリクエストエントリを確認する
    request = state.get_entry('user', 'id_request')
    
    # フラグが True の場合のみ処理を実行する
    if request['flag']:
        length = request['value']
        
        # ID生成ロジック
        chars = string.ascii_letters + string.digits
        new_id = ''.join(random.choice(chars) for _ in range(length))
        
        # 自身の処理結果をフラグ True で書き込む
        state.update('generator', 'result_id', new_id, True)
        
        print(f"ID生成成功: {new_id}")
        
        # 処理が終わったので、ユーザー側のリクエストフラグを False に戻す（フラグの回収）
        # 値はそのままでも、フラグが False なら ui_input は次の入力を受け付けられる
        state.update('user', 'id_request', length, False)