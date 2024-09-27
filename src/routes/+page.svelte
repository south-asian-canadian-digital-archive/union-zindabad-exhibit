<script lang="ts">
  import { goto } from "$app/navigation";
  import { base } from "$app/paths";
  import { onMount } from "svelte";

  const logos = [
    {
      name: "South Asian Studies Institute",
      link: "http://www.ufv.ca/sasi",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/sasi.svg",
    },
    {
      name: "University of the Fraser Valley",
      link: "http://www.ufv.ca/",
      image:
        "https://sacda.ca//themes/sacda/assets/pawtucket/graphics/footer/ufv.svg",
    },
    {
      name: "BC Labour Heritage Centre",
      link: "https://www.labourheritagecentre.ca/",
      image: "/images/preface_img_0.png",
    },
    {
      name: "Province of British Columbia",
      link: "https://www2.gov.bc.ca/",
      image:
        "https://sacda.ca/themes/sacda/assets/pawtucket/graphics/footer/bc.svg",
    },
  ];

  let coverELm: HTMLElement;

  onMount(() => {
    setTimeout(() => {
      if (coverELm) {
        coverELm.scrollIntoView({ behavior: "smooth" });
      }
    }, 1000);
  });
</script>

<div
  class="bg-[url(/images/cover_img_0.jpg)] bg-cover h-full selection:bg-black selection:bg-opacity-50 selection:text-white"
  bind:this={coverELm}
>
  <div
    class="bg-cover h-screen w-full p-8 flex flex-col justify-end text-white bg-[#5c5c5c] bg-opacity-20"
  >
    <div class="flex flex-col items-center gap-4 pt-10">
      <div class="text-8xl z-10 font-mono pt-10 font-bold">
        <p>UnionZindabad!</p>
        <p class="text-base text-center">
          South Asian Canadian Labour History in British Columbia
        </p>
      </div>

      <div class="flex gap-4">
        <button
          class="rounded-lg p-2 px-6 font-bold bg-white border border-black text-[#000000D1] -translate-y-1 translate-x-1 hover:-translate-y-2 hover:translate-x-2 transition-all duration-500 ease-in-out"
          on:click={() => {
            goto("./south-asian-canadian-labour-history-project");
          }}>Read Book</button
        >
        <a href="https://sacda.ca/index.php/Detail/collections/746">
          <button
            class="rounded-lg p-2 px-6 font-bold bg-white border border-black text-[#000000D1] -translate-y-1 translate-x-1 hover:-translate-y-2 hover:translate-x-2 transition-all duration-500 ease-in-out"
          >
            View the Collection
          </button>
        </a>
      </div>

      <div
        class="lg:text-base md:text-base mt-8 lg:mt-0 md:mt-0 text-xs text-center max-w-[70vw] flex flex-col gap-4"
      >
        Union Zindabad traces South Asian labor history in Canada through a
        variety of lenses. Beginning with the migrations of the early twentieth
        century, this book includes chapters on early migrants, revolutionaries,
        unions, and the struggles of South Asian labor activists and leaders.
      </div>
    </div>
  </div>
</div>

<style type="postcss">
  /* p a {
    @apply border-b border-b-white transition-all ease-in-out duration-200 hover:border-b-transparent;
  } */

  .text-shadow {
    text-shadow: -12px 11px 4px rgba(0, 0, 0, 0.25);
    /* font-family: 'Lexend Peta', sans-serif !important; */
  }
</style>
