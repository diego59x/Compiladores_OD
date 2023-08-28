class Main inherits IO {
  var : Bool <- true;

  main() : Object {
    if var then {
      out_string("Hello, World.\n");
    } else {
      out_string("Hello, World 2.\n");
    } FI
  };
};