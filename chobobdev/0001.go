func solution(n int) string {
	var answer string
	if n%2 == 0 {
		for i := 0; i < n/2; i++ {
			answer += "수박"
		}
	} else {
		for i := 0; i < (n-1)/2; i++ {
			answer += "수박"
		}
		answer += "수"
	}

	return answer
}