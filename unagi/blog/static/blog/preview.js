document.addEventListener("DOMContentLoaded", fillPreview);

const fieldsToMonitor = [
    "id_title",
    "id_cover_image_url",
    "id_content",
];

// Add event listeners to all fields that should trigger a preview update.
fieldsToMonitor.forEach((field) => {
    document.getElementById(field).addEventListener("input", fillPreview);
});

/**
 * Fill the preview container with the updated content based on user input.
 * @param {Event} event - The event that triggered the function.
 */
function fillPreview(event) {
    const title = document.getElementById("id_title").value;
    const cover_image_url = document.getElementById("id_cover_image_url").value;
    const content = document.getElementById("id_content").value;

    document.getElementById("preview-container").innerHTML = `
        <div id="post-container" class="centered-flex-container">
            <a href="#" class="flat-link"><</a>
            <h1>${title}</h1>
            <p class="meta-info">Published on ${new Date().toLocaleString()}</p>
            ${
                cover_image_url
                    ? `
                <img id="cover-image" src=${cover_image_url} width=500/>
            `
                    : ""
            }
            ${content}
        </div>
    `;
}
