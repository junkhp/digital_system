# -*- coding: utf-8 -*-
from pprint import pprint


class SolveKnapsackProblem():
    def set_problem(self):
        self.n = 5
        # self.I = [[1, 2], [8, 20], [10, 21], [2, 4], [3, 2], [5, 8], [4, 4]]
        self.I = [[1, 2], [8, 20], [2, 3], [2, 4], [3, 2]]
        self.B = 5
        self.mu = 1
    
    def preparation(self):
        epsilon = 0.5
        M = 0
        for i in self.I:
            if i[1] > M:
                M = i[1]
        mu = epsilon * M / self.n
        for i in range(len(self.I)):
            self.I[i][1] = int(self.I[i][1] / mu)
        self.M = M
        self.mu = mu
        self.epsilon = epsilon
    
    def remove_dominated_pair(self, j):
        remove_index = set()
        A_j = self.A[j]
        for i in range(len(A_j) - 1):
            for k in range(i + 1, len(A_j)):
                t_i, t_k = A_j[i][0], A_j[k][0]
                w_i, w_k = A_j[i][1], A_j[k][1]
                if (t_i <= t_k) and (w_i >= w_k):
                    remove_index.add(k)
        for i, k in enumerate(remove_index):
            self.A[j].pop(k - i)

    def dynamic_programming(self):
        self.A = [[[0, 0], self.I[0]]]
        for j in range(1, self.n):
            # print(j + 1)
            # print(self.I[j])
            self.A.append(self.A[j - 1].copy())
            s_j = self.I[j][0]
            v_j = self.I[j][1]
            for t, w in self.A[j - 1]:
                if t + s_j <= self.B:
                    self.A[j].append([t + s_j, w + v_j])
            # print(self.A[j])
            self.remove_dominated_pair(j)
            # print(self.A[j])
        # pprint(self.A)
        ans = 0
        for i in self.A[-1]:
            if i[1] > ans:
                ans = i[1]
        # print(ans)
        self.ans = int(ans * self.mu)


def main():
    knapsack = SolveKnapsackProblem()
    knapsack.set_problem()
    knapsack.preparation()
    print(knapsack.I)
    knapsack.dynamic_programming()
    print(knapsack.ans)


if __name__ == "__main__":
    main()
