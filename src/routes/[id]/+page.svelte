<script lang="ts">
  import ContentList from "$lib/utils/contents";
  import { page } from "$app/stores";
  import { goto } from "$app/navigation";

  const findContent = (id: string) => {
    for (let i = 0; i < ContentList.length; i++) {
      if (ContentList[i].id === id) {
        return ContentList[i];
      }

      let chapters = ContentList[i].chapters;
      if (chapters) {
        for (let j = 0; j < chapters.length; j++) {
          if (chapters[j].id === id) {
            return chapters[j];
          }
        }
      }
    }

    goto("/404");
  };

  $: siteContent = findContent($page.params.id);
</script>


<style type="postcss">
	:global(h2.entry-title) {
		@apply text-3xl text-center py-4;
	}

</style>

<main class="w-1/2">

  <div id="site-content" class="text-lg font-serif">
    {@html siteContent?.content}
  </div>
</main>
