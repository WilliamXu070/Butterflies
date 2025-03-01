// Path where the images are stored
const imageFolder = "images/"; // Change this to the correct path

// Array to store image file names (you would get this dynamically from your server)
const images = [
  "107-80.png",
  "Screenshot 2024-10-21 at 4.46.03 PM.png",
]; // Replace with real image names or dynamically load them

let currentIndex = 0;

const image1 = document.getElementById("image1");
const image2 = document.getElementById("image2");

function loadImage(src, callback) {
  const img = new Image();
  img.src = src;
  
  img.onload = () => {
    callback(img);
  };

  img.onerror = () => {
    console.error("Failed to load image:", src);
  };
}

function updateImages() {
  // Create image 1
  loadImage(`${imageFolder}${images[currentIndex]}`, (img1) => {
    image1.src = img1.src;  // Set image1 src after it has loaded

    // Load image 2 after image 1 is loaded
    loadImage(`${imageFolder}${images[(currentIndex + 1) % images.length]}`, (img2) => {
      image2.src = img2.src;  // Set image2 src after it has loaded

      // Reset the second image to its original state before applying new styles
      image2.classList.remove("greyed-out");
      image2.style.transform = "translateX(50%)"; // Reset the "cut-off" transform

      // Apply the gray-out and transition effect on image2
      setTimeout(() => {
        image2.classList.add("greyed-out");
      }, 50);
    });
  });
}

// Next button click handler
document.getElementById("next").addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % images.length;
  updateImages();
});

// Previous button click handler
document.getElementById("prev").addEventListener("click", () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateImages();
});

// Initial load of images
updateImages();
