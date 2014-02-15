$(document).ready(function() {
	// We checks for side menu toggle button visibilty
	if(!$("#side-menu-header button").is(":hidden")) {
		// If it is visible, we collapse the menu
		$("#side-menu-content").removeClass("in");
		$("#side-menu-content").addClass("out");
	}
});