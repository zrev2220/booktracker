"use strict";

// declare jQuery vars
let $addAuthorBtn, $removeAuthorBtn, $addCategoryBtn, $removeCategoryBtn;

$(() => {
  // initialize jQuery vars
  // note: window.authorId and window.categoryId are set in inline script in book_form.html
  $addAuthorBtn = $(`#add-entry-${window.authorId}`);
  $removeAuthorBtn = $(`#remove-entry-${window.authorId}`);
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
