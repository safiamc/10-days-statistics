from scipy.stats import binom
n = 6
p = 1.09/2.09
cumulative_sum=0
for r in range(3,7):
  cumulative_sum += binom.pmf(r, n, p)
print(round(cumulative_sum,3))
