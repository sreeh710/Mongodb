<!DOCTYPE html>
<html>
<head>
<title>Hello_World</title>
</head>
<body>
<p>
Welcome:{{username}}
</p>
<ul>
% for thing in things:
<li> {{thing}}</li>
%end
</ul>
<form action="/fav_fruit" method="POST">
What is your favourite fruit?
<input type="text" name="fruit" size="40" value=""/><br>
<input type="submit" value="submit">
</form>
</body>
</html>