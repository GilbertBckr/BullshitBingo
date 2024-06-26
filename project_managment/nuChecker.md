# Nu Checker Erklärung

## "A document must not include both a meta element with an http-equiv attribute whose value is content-type, and a meta element with a charset attribute"

Der `charset` Meta Tag wird von uns gesetzt, der `http-equiv` Tag wird dagegen von `vue.js` gesetzt. Unseren Tag zu entfernen ist leider keine Lösung, da `vue.js` diesen nutzt um den `http-equiv` Tag zu erstellen (warum auch immer...). Es scheint jedoch bei allen großen Browsern keine Probleme zu geben.

## "CSS: padding-left: Parse Error" & "CSS: --: Parse Error"

Dieses Error entsteht, da in der Berechnung von `padding-left` eine var nutzt die von `vue.js` verwaltet wird und deshalb mit Nummern beginnt. Das ist nach [den Specs](https://www.w3.org/TR/css-variables-1/#defining-variables) aber erlaubt.
