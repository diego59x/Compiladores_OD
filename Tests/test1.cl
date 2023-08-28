class Main inherits IO {
  var : String <- "string";

  add_counter(var : Int ) : Int {
    {
      var <- 1;
      var + 1;
    }
  };

  main() : Object {
    add_counter(10)
  };
};