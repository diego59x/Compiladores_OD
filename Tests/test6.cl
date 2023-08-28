class Main inherits IO {
  var1 : Int <- 0;
  var2 : Int <- 0;
  var3 : String <- "Hola Mundo";

  suma(num1 : Int) : Int {
    num1 + var2
  };

  main() : Object {
    var3 <- suma(1)
  };
};