class Solution:
    def encode(self, strs: list[str]) -> str:
        """文字列のリストを1つの文字列にエンコードする"""
        res = ""
        for s in strs:
            # "文字数" + "#" + "実際の文字列" の形で結合する
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        """エンコードされた文字列を元のリストにデコードする"""
        res = []
        i = 0  # 現在読み込んでいる文字の位置（ポインタ）
        
        while i < len(s):
            # iの位置以降で、最初に現れる '#' のインデックスを取得
            j = s.find('#', i)
            
            # iからjまでの部分が「文字数」を表す数字
            length = int(s[i:j])
            
            # '#' の次の文字(j+1)から、取得した文字数分だけスライスして抽出
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # 読み込み位置を、次の単語の先頭に更新する
            i = j + 1 + length
            
        return res