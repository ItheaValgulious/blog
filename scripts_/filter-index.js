hexo.extend.generator.register('index', function (locals) {
  const excludeTags=["homework"]

  // var posts = locals.posts.filter(post => post.tags.some(tag => includeTag.includes(tag)));
  var posts = locals.posts.filter(post => !post.tags.some(tag => excludeTags.includes(tag)));

  return {
    path: '',
    layout: ['index'],
    data: { posts }
  };
});
