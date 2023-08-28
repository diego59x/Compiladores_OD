class Suma {
  var : Int <- 0;

  suma(num1 : Int) : Int {
    var + num1
  };
};

class SumaHija inherits Suma {
  var2 : Int <- 0;

  suma(num1 : Int, num2 : Int) : Int {
    {
      num1 + num2;
    }
  };
};

class Main inherits IO {
  instancia: Suma;
  main(): Object {
    {
      instancia <- new Suma
    };
  }
};