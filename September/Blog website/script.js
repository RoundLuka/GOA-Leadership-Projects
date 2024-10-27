const addBlogButton = document.getElementById("add-blog");
const blogsDiv = document.getElementById("newBlog");

const blogs = {};
let blogCount = 2;

function addBlog(){
    const blog = document.createElement("div");
    blog.className = "blog-post";
    blog.id = "blog" + blogCount;

    const profile = document.createElement("div");
    profile.className = "profile";
    profile.id = "profile" + blogCount;


    const imgInput = document.createElement("input");
    imgInput.type = "text";
    imgInput.placeholder = "Image Source (Profile Picture)";
    
    const userHeaderInput = document.createElement("input");
    userHeaderInput.type = "text";
    userHeaderInput.placeholder = "Your Name";

    const quoteCheckbox = document.createElement("input");
    quoteCheckbox.id = "checkboxInput" + blogCount;
    quoteCheckbox.type = "checkbox";
    
    const quoteLabel = document.createElement("label");
    quoteLabel.textContent = "Include decorative quotes";

    const blogContent = document.createElement("div");
    blogContent.className = "blog-content";

    const blogText = document.createElement("textarea");
    blogText.placeholder = "Your text here";

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Cancel';

    const confirmButton = document.createElement('button');
    confirmButton.textContent = 'Confirm';

    profile.append(imgInput);
    profile.append(userHeaderInput);
    profile.append(quoteLabel);
    profile.append(quoteCheckbox);

    blogContent.append(blogText);
    blogContent.append(cancelButton);
    blogContent.append(confirmButton);

    blog.append(profile);
    blog.append(blogContent);

    blogsDiv.append(blog);
    
    confirmButton.addEventListener
}

addBlogButton.addEventListener("click", addBlog);