(function() {
    'use strict';

    angular
        .module('app.interventions')
        .config(configFunction);

    configFunction.$inject = ['$routeProvider', 'STATIC_URL'];

    function configFunction($routeProvider, STATIC_URL) {
        $routeProvider.when('/interventions', {
            templateUrl: STATIC_URL + '/interventions/interventions.html',
            controller: 'CommandsController',
            controllerAs: 'vm',
            resolve: {isLoggedIn: resolveUser}
        });
    }

    resolveUser.$inject = ['authService'];

    function resolveUser(authService) {
        return authService.isLoggedIn();
    }
})();
