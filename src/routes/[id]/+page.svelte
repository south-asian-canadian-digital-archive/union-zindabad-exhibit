<script lang="ts">
  import { goto } from "$app/navigation";
  import { page } from "$app/stores";
  import ContentList from "$lib/utils/contents_";
  import { pageIdx } from "$lib/utils/nav.store";

  // let $pageIdx = 0;

  const findContent = (id: string) => {
    for (let i = 0; i < ContentList.length; i++) {
      if (ContentList[i].id === (id.endsWith(".html") ? id.slice(0, -5) : id)) {
        $pageIdx = i;
        return ContentList[i];
      }

      let chapters = ContentList[i].chapters;
      if (chapters) {
        for (let j = 0; j < chapters.length; j++) {
          if (chapters[j].id === (id.endsWith(".html") ? id.slice(0, -5) : id)) {
            $pageIdx = i + (j + 1) / 100;
            return chapters[j];
          }
        }
      }
    }

    // goto("/404");
  };

  $: siteContent = findContent($page.params.id);
</script>

{#if $page.params.id === "media"}
  <div>media</div>
{:else}
  {@html siteContent?.content}
{/if}
