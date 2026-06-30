def topKFrequent(nums: list[int], k: int) -> list[int]:
    # 1. 出現回数をカウント
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        
    # 2. 出現回数をインデックスとしたバケットを作成
    # バケットのサイズは最大で len(nums) + 1
    freq = [[] for i in range(len(nums) + 1)]
    for num, c in count.items():
        freq[c].append(num)
        
    # 3. 後ろからk個取り出す
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res