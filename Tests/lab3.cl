class Main inherits IO {
  var1 : Int <- 2;
  var2 : Int <- 2;
  var3 : Int <- 0;

  main() : Object {
    {
      var3 <- var1 + var2;
      var3 <- var1 - var2;
      var3 <- var1 * var2;
      var3 <- var1 / var2;
    }
  };
};