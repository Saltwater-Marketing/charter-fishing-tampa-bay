export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/images");
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });
  eleventyConfig.addCollection("reports", (c) => c.getFilteredByGlob("src/fishing-reports/*.md").sort((a, b) => b.date - a.date));
  eleventyConfig.addCollection("guides", (c) => c.getFilteredByGlob("src/fishing-guides/*.md"));
  eleventyConfig.addFilter("monthYear", (d) => new Date(d).toLocaleDateString("en-US", { month: "long", year: "numeric", timeZone: "UTC" }));
  eleventyConfig.addFilter("head", (a, n) => a.slice(0, n));
  eleventyConfig.addFilter("isoDate", (d) => new Date(d).toISOString().slice(0, 10));
  return { dir: { input: "src", output: "_site" }, markdownTemplateEngine: "njk", htmlTemplateEngine: "njk" };
}
