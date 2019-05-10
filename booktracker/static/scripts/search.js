$(function() {
    console.log("We're ready, here we go!!");
    $("#moreFiltersBtn").on("click", toggleMoreFilters);
});

function toggleMoreFilters() {
    let btn = $("#moreFiltersBtn");
    let moreHidden = $("#moreFiltersHidden");
    let div = $("#moreFilters");
    let icon = "minus";
    let text = "Fewer filters";
    if (div.hasClass("show")) {
        icon = "plus";
        text = "More filters";
        moreHidden.val("False");
    }
    else {
        moreHidden.val("True");
    }
    console.log("Before:", btn.html());
    console.log("I propose:", `<i class="fas fa-${icon}"></i> ${text}`);
    btn.html(`<i class="fas fa-${icon}"></i> ${text}`);
    console.log("After:", btn.html());
}
