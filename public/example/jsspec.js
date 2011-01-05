function hello() {
	return 'hello';
}


describe('hello', {
	'should be hello': function() {
		value_of(hello()).should_be('hello');
	}
});
