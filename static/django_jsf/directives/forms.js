angular.module("jsf.forms", ["jsf.tpls","jsf.directives"]);
angular.module("jsf.tpls", ["template/jsf/form.html"]);

angular.module('jsf.directives', ["schemaForm"])
.directive('notificationSubscription', function(Subscription,Notification) {
	  return {
	    restrict: 'AE',
	    templateUrl: "template/jsf/form.html",
	    scope: {
	    	objectId:'@',
	    	contentType:'@'
	    },
	    controller: function($scope, $http, $element){
	    	this.$scope = $scope;
	    }
	  }
	});


angular.module("template/jsf/form.html", []).run(['$templateCache', function($templateCache) {
	  $templateCache.put("template/jsf/form.html",
	'  <form name="myForm"\
	          sf-schema="schema"\
	              sf-form="form"\
	              sf-model="model"\
	              ng-submit="onSubmit(myForm)"></form>'
	  );
	}]);

