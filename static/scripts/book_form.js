"use strict";

// declare jQuery vars
let $addAuthorBtn, $removeAuthorBtn, $addAuthorModal, $addCategoryBtn, $removeCategoryBtn;

$(() => {
  // initialize jQuery vars
  // note: window.authorId and window.categoryId are set in inline script in book_form.html
  $addAuthorBtn = $(`#add-entry-${window.authorId}`);
  $removeAuthorBtn = $(`#remove-entry-${window.authorId}`);
  $addAuthorModal = $("#add-author-modal");
  $addCategoryBtn = $(`#add-entry-${window.categoryId}`);
  $removeCategoryBtn = $(`#remove-entry-${window.categoryId}`);

  // register event handlers
  // register change handler for target of each remove button
  $.each([$removeAuthorBtn, $removeCategoryBtn], (i, btn) => {
    btn = $(btn);
    const targetInput = $(btn.data("target"));
    targetInput.on("change", e => onModifiableInputChanged(btn, $(e.target).val()));
    // fire the change handler once to initialize button state
    onModifiableInputChanged(btn, targetInput.val());
  });

  // Register author form submit handler
  $addAuthorModal.find("form").on("submit", e => onAuthorFormSubmit(e));
  // Register author form dismiss handler; clear inputs after dismissal
  $addAuthorModal.on("hide.bs.modal", e => $(e.target).find(".modal-body input").val(""));
});

/**
 * Change handler for modifiable inputs--i.e. those accompanied by add/remove buttons.
 *
 * Enables/disables the input's `disabled` property according to its value, empty or nonempty.
 * @param btn {HTMLButtonElement}
 * @param value {string[]}
 */
function onModifiableInputChanged(btn, value) {
  // enable/disable remove button if something/nothing is selected
  btn.prop("disabled", value.length === 0);
}

/**
 * Submit handler for add author form.
 *
 * Makes an AJAX request to add an author. On success, adds the author to the top of the author select box and scrolls
 * the new option into view.
 * @param e {Event} Add author form's submit event.
 */
function onAuthorFormSubmit(e) {
  e.preventDefault();
  const $form = $(e.target);
  const data = {};
  $form.serializeArray().forEach(obj => data[obj.name] = obj.value);
  $.post({
    url: window.addAuthorUrl,
    headers: {"X-CSRF-Token": data["crsfmiddlewaretoken"]},
    data,
    success: response => {
      if (response["errors"]) {
        // display error messages
        const $errorContainer = $addAuthorModal.find(".error-div");
        $errorContainer.html("");  // clear previous errors
        response["errors"].forEach(errorMsg => $errorContainer.append(`<small class="text-danger">${errorMsg}</small>`));
      } else {
        // add author to list
        const {id, full_name} = response["author"];
        const $authorSelect = $("#" + window.authorId);
        $authorSelect.prepend(`<option value="${id}">${full_name}</option>`);
        // scroll new author into view
        // see https://stackoverflow.com/a/7206039/6548555
        $authorSelect.scrollTop($authorSelect.find(`option[value=${id}]`).offset().top - $authorSelect.offset().top);
        // dismiss modal
        $addAuthorModal.modal("hide");
      }
    },
  });
}
