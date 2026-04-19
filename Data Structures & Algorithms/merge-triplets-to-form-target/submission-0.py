class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goodTripletsF = []
        goodTripletsS = []
        goodTripletsT = []

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
               next 
            else:
                goodTripletsF.append(triplet[0])
                goodTripletsS.append(triplet[1])
                goodTripletsT.append(triplet[2])
        
        return target[0] in goodTripletsF and target[1] in goodTripletsS and target[2] in goodTripletsT