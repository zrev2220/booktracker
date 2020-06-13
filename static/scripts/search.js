"use strict";

/**
 * Set of currently-displayed filters.
 * @type {Set<string>}
 */
let filters;
/**
 * Set of div elements which have triggered a collapse process that has not finished yet.
 *
 * This is used to prevent rapid clicks causing a button's appearance to become inconsistent with its div's collapse
 * state.
 * @type {Set<HTMLDivElement>}
 */
const collapsingFilters = new Set();

$(() => {
  // register event handlers
  $("#searchForm").on("submit", e => onFormSubmit(e));
  const $filterBtns = $(".filter-btn").on("click", e => toggleFilter(e.target));
  $(".collapse").on("shown.bs.collapse hidden.bs.collapse", e => collapsingFilters.delete(e.target));

  // make sure active filters' buttons are initialized
  filters = new Set(JSON.parse($("#activeFilters").val()));
  for (const btn of Array.from($filterBtns).filter(b => filters.has($(b).data("filter")))) {
    toggleFilter(btn, true);
    $(btn.dataset.target).collapse("show");
  }

  // if and/or is set to or, toggle button to switch text
  if ($("#andOrHidden").val() === "or")
    $("#andOrBtn").text("Results match ANY filter");
});

function onFormSubmit(e) {
  e.preventDefault();
  console.log(e);

  const $form = $("#searchForm");
  const data = {};
  $form.serializeArray().forEach(obj => data[obj.name] = obj.value);
  $.post({
    url: "/search",
    headers: {"X-CSRFToken": data["csrfmiddlewaretoken"]},
    data: data,
    success: data => $("#resultsBody").html(data.html),
  });
  return false;
}

function toggleFilter(btn, init = false) {
  const thisFilter = btn.dataset.filter;
  const $filterElement = $(btn.dataset.target);
  if (!collapsingFilters.has($filterElement[0]) || init) {
    if (!init) {
      // if not init'ing, add the target div to collapsingFilters to ignore additional clicks until animation completes
      collapsingFilters.add($filterElement[0]);
    }
    const $filterInput = $("#activeFilters");
    btn.classList.toggle("btn-outline-primary");
    btn.classList.toggle("btn-primary");
    if (!init) {
      if (filters.has(thisFilter))
        filters.delete(thisFilter);
      else
        filters.add(thisFilter);
    }
    $("#searchBtn").prop("disabled", filters.size === 0);
    $("#andOrDiv").collapse(filters.size > 1 ? "show" : "hide");
    $filterInput.val(JSON.stringify(Array.from(filters)));
  }
}

function toggleAndOr() {
  const $btn = $("#andOrBtn");
  const $hidden = $("#andOrHidden");
  let text, val;
  if ($hidden.val() === "and") {
    text = "Results match ANY filter";
    val = "or";
  } else {
    text = "Results match ALL filters";
    val = "and";
  }
  $btn.text(text);
  $hidden.val(val);
}
