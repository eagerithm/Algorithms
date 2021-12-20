package main

import "fmt"

func main () {
	dogs := [] string{"|\\_/|", "|q p|   /}", "( 0 )\"\"\"\\", "|\"^\"`    |","||_/=\\\\__|"}
	for _, dog := range dogs {
		fmt.Println(dog)         
    }
}