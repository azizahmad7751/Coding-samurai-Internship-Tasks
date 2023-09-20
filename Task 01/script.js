let display = document.getElementById('display');
let expression = '';

function appendChar(char) {
  expression += char;
  display.value = expression;
}

function calculate() {
  try {
    let result = eval(expression);
    display.value = result;
    expression = result;
  } catch (error) {
    display.value = 'Error';
    expression = '';
  }
}

function clearDisplay() {
  expression = '';
  display.value = '';
}
