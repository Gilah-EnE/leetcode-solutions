class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.fill(image, sr, sc, color, image[sr][sc])
        
        return image
    
    def fill(self, image, sr, sc, newcolor, color):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or color != image[sr][sc] or newcolor == image[sr][sc]:
            return None

        image[sr][sc] = newcolor

        self.fill(image, sr + 1, sc, newcolor, color)
        self.fill(image, sr, sc + 1, newcolor, color)
        self.fill(image, sr - 1, sc, newcolor, color)
        self.fill(image, sr, sc - 1, newcolor, color)
