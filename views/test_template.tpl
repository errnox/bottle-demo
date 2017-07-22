<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Template Engine Test</title>
  </head>

<body>
  <h1>Template Engine Test</h1>
  <h2>Some random things</h2>
  <ul>
    <li>apple</li>
    <li>banana</li>
    <li>skateboard</li>
    <li>house</li>
  </ul>
  <h2>Info</h2>
  <p>You came here and brougth with you: "{{name}}"</p>

%if query_variables:
  <h1>Query variables</h1>
<p>\\
%for var in query_variables:
  <p>{{var}}</p>\\
%end
</p>
%end


</body>

</html>
