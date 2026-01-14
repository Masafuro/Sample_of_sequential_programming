from state import state

def wait_for_input():
    # 既にリクエストのフラグが True なら、処理が進行中とみなしてスキップ
    current_request = state.get_entry('user', 'hash_request')
    if current_request['flag']:
        return

    user_val = input("ハッシュ化したい文字列を入力してください: ")
    
    if user_val:
        # 文字列を受け取り、フラグを TRUE にする
        state.update('user', 'hash_request', user_val, True)