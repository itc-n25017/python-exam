days = ['月', '月', '火', '水', '木', '金', '金']

days.remove('月')  # 重複している月を1つ削除する
days.remove('金')  # 重複している金を1つ削除する

days.insert(0, '日')  # リストの先頭に日を追加する
days.insert(6, '土')  # インデックス6に土を追加する

print(days)