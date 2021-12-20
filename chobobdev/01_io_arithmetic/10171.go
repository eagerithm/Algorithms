package main

import "fmt"

func main () {
	cats := [] string{"\\    /\\", " )  ( ')", "(  /  )", " \\(__)|"}
	for _, cat := range cats {
		fmt.Println(cat)         
    }
}