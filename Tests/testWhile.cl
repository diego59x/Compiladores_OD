class Main {
  	num : Int <- 1;
	x : Int <- 1;
  	main() : Object {
      
      (let y : Int <- 1 in
	       while y <= num loop
	          {
              x <- x * y;
              y <- y + 1;
	          }
	       pool
	    )
      
   };
  
};