$().ready(() => {
  $("#searchForm").on("submit", e => onFormSubmit(e));
  let $filterBtns = $(".filter-btn").on("click", e => toggleFilter(e.target));

  // make sure active filters' buttons are initialized
  let filters = new Set(JSON.parse($("#activeFilters").val()));
  for (let btn of Array.from($filterBtns).filter(b => filters.has($(b).data("filter")))) {
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

  let $form = $("#searchForm");
  let data = {};
  $form.serializeArray().forEach(obj => data[obj.name] = obj.value);
  $.post({
    url: "/search",
    headers: {"X-CSRFToken": data["csrfmiddlewaretoken"]},
    data: data,
    success: displayResults,
  });
  return false;
}

function displayResults(data) {
  let $table = $("#resultsTable");
  let $noResults = $("#noResultsLabel");
  if (data.items.length > 0) {
    $table.removeClass("d-none");
    $noResults.addClass("d-none");
    let $tbody = $("#resultsBody").html("");
    for (let book of data.items) {
      let nameParts = [];
      if (book.author_last) nameParts.push(book.author_last);
      if (book.author_first) nameParts.push(book.author_first);
      let name = nameParts.join(", ");
      let row = $("<tr></tr>").toggleClass("checked-out", book.checkout);
      row.append(`<td>${name}</td>`,
                 `<td>${book.title}</td>`,
                 `<td class="d-none d-sm-table-cell">${book.location}</td>`);
      $tbody.append(row);
    }
  } else {
    $table.addClass("d-none");
    $noResults.removeClass("d-none");
  }
}

function toggleFilter(btn, init=false) {
  let thisFilter = btn.dataset.filter;
  let $filterInput = $("#activeFilters");
  btn.classList.toggle("btn-outline-primary");
  btn.classList.toggle("btn-primary");
  let filters = new Set(JSON.parse($filterInput.val()));
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

function toggleAndOr() {
  let $btn = $("#andOrBtn");
  let $hidden = $("#andOrHidden");
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
