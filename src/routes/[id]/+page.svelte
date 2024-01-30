<script lang="ts">
  import site_contents from "$lib/utils/contents";
  import { page } from "$app/stores";

  const findContent = (id: string) => {
    for (let i = 0; i < site_contents.length; i++) {
      if (site_contents[i].id === id) {
        return site_contents[i].content;
      }

      let chapters = site_contents[i].chapters;
      if (chapters) {
        for (let j = 0; j < chapters.length; j++) {
          if (chapters[j].id === id) {
            return chapters[j].content;
          }
        }
      }
    }
  };

  $: content = findContent($page.params.id);
</script>



