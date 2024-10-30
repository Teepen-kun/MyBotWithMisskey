
from misskey import Misskey
from config import Config

def main():    
    api = Misskey('misskey.io')
    api.token = Config.API_KEY

    username = Config.USER_ID
    user_id = get_user_id(api, username)

    if user_id:
        notes = get_notes(user_id, api)
    else:
        print("ノートを取得できませんでした.ユーザーIDが無効です.")
    #create_notes(api, notes)

    
    

def get_user_id(api, username):
    user_info = api.users_show(username = username)
    if user_info:
        return user_info['id']  # 最初のユーザーのIDを取得
    else:
        print("ユーザーが見つかりませんでした")
        return None


def get_notes(user_id, api, limit = 50):
    notes = api.users_notes(user_id=user_id, limit=limit, include_replies=False)
    
    note_texts = [note['text'] for note in notes]  # 各ノートのテキストをリストとして取得
    
    for text in note_texts:
        print(text)
    return note_texts  # ノートのリストを返す

def create_notes(api, notes):
    #note = input()
    text = '\n'.join(notes)  # リストを改行で結合
    api.notes_create(text=text)  # 新しいノートを作成

if __name__ == "__main__":
    main()