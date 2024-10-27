const addBlogButton = document.getElementById("add-blog");
const newBlogDiv = document.getElementById("newBlog");
const blogsDiv = document.getElementById("content");


const blogs = {};
let blogCount = 2;

let BlogInProcess = false;

function addBlog(){
    if (BlogInProcess) {
        return;
    }
    BlogInProcess = true;
    const blog = document.createElement("div");
    blog.className = "newBlog";

    const profile = document.createElement("div");
    profile.className = "profile";


    const imgInput = document.createElement("input");
    imgInput.type = "text";
    imgInput.id = "imgInput";
    imgInput.placeholder = "Image Source (Profile Picture)";
    
    const userHeaderInput = document.createElement("input");
    userHeaderInput.type = "text";
    userHeaderInput.placeholder = "Your Name";

    const quoteCheckbox = document.createElement("input");
    quoteCheckbox.type = "checkbox";
    
    const quoteLabel = document.createElement("label");
    quoteLabel.textContent = "Include decorative quotes";

    const blogContent = document.createElement("div");
    blogContent.className = "blog-content";

    const blogText = document.createElement("textarea");
    blogText.placeholder = "Your blog text here";
    blogText.cols = 25
    blogText.rows = 5

    const countBox = document.createElement("p");
    countBox.textContent = "0/200";
    countBox.style.display = "inline";

    const cancelButton = document.createElement('button');
    cancelButton.textContent = 'Cancel';

    const confirmButton = document.createElement('button');
    confirmButton.textContent = 'Confirm';

    const breakLine = document.createElement("br");

    profile.append(imgInput);
    profile.append(userHeaderInput);
    profile.append(quoteLabel);
    profile.append(quoteCheckbox);

    blogContent.append(blogText);
    blogContent.append(cancelButton);
    blogContent.append(confirmButton);
    blogContent.append(breakLine);
    blogContent.append(countBox);

    blog.append(profile);
    blog.append(blogContent);

    newBlogDiv.append(blog);
    
    blogText.addEventListener("input", () => counter(blogText, countBox));

    cancelButton.addEventListener("click", () => {
        blog.remove();
        BlogInProcess = false;
    });

    confirmButton.addEventListener("click", () => {

        const currentCount = blogText.value.length; 
        if (currentCount > 305) {
            countBox.style.color = "red"; 
            countBox.textContent = "Character limit exceeded"; 
            return; 
        }

        if (userHeaderInput.value < 3) {
            countBox.textContent = "Header must have at least length of 4"; 
            return; 
        }

        if (currentCount < 20) {
            countBox.textContent = "Blog text length must be at least 20"; 
            return; 
        }
        
        const resultBlog = document.createElement("div");

        resultBlog.className = "blog-post";
        resultBlog.id = "blog" + blogCount;

        const resultBlogProfile = document.createElement("div");
        resultBlogProfile.className = "profile";

        const resultBlogContent = document.createElement("div");
        resultBlogContent.className = "blog-content";

        const profileImage = document.createElement("img");
        profileImage.src = imgInput.value;
        profileImage.alt = "Profile Picture";


        const userName = document.createElement("h4");
        if(userHeaderInput.value !== ""){
            userName.textContent = userHeaderInput.value;
        }
        else {
            userName.textContent = "Unknown";
        }

        const blogPostText = document.createElement("p");
        blogPostText.textContent = blogText.value;



        resultBlogProfile.append(profileImage);
        resultBlogProfile.append(userName); 

        resultBlogContent.append(blogPostText);

        resultBlog.append(resultBlogProfile);
        resultBlog.append(resultBlogContent);

        blogsDiv.append(resultBlog);

        blog.remove();

        BlogInProcess = false;
    });
}

function counter(blogText, countBox){
    const limit = 305;
    let current_count = blogText.value.length

    if(current_count > limit){
        countBox.style.color = "red"
        countBox.textContent = "Character limit exceeded";
    }
    else{
        countBox.style.color = "rgba(127, 255, 180, 0.945)";
        countBox.textContent = current_count + "/" + limit;
    }
}

addBlogButton.addEventListener("click", addBlog);