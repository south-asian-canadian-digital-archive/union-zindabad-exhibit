<script>
  import { goto } from "$app/navigation";
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

  onMount(() => {
    // goto("./cover");
  });
</script>

<div
  class="bg-[url(/cover_bg.jpg)] p-6 md:p-20 lg:p-20 bg-cover h-full selection:bg-black selection:bg-opacity-50 selection:text-white"
>
  <div
    class="flex flex-col lg:flex-row md:flex-row overflow-clip justify-center gap-16"
  >
    <div class="flex flex-col gap-10 pt-10">
      <div class="text-7xl z-10 text-shadow font-lexend-peta text-white pt-10">
        <p>Union</p>
        <p class="">Zindabad!</p>
        <p class="text-sm pt-4">South Asian Canadian Labour History in British Columbia</p>
      </div>

      <div class="lg:hidden md:hidden w-[80vw] -my-4 self-end">
        <img src="/cover_right.png" alt="" class="" />
      </div>

      <div class="w-full flex justify-evenly pt-4">
        <div class="bg-black rounded-lg w-fit z-10">
          <button
            class="rounded-lg p-2 px-6 md:text-lg lg:text-lg font-bold bg-white border border-black text-[#000000D1] -translate-y-1 translate-x-1 hover:-translate-y-2 hover:translate-x-2 transition-all duration-500 ease-in-out"
            on:click={() => {
              goto("/south-asian-canadian-labour-history-project");
            }}>Read Book</button
          >
        </div>

        <div class="bg-black rounded-lg w-fit z-10">
          <a href="https://sacda.ca/index.php/Detail/collections/746">
            <button
              class="rounded-lg p-2 px-6 md:text-lg lg:text-lg font-bold bg-white border border-black text-[#000000D1] -translate-y-1 translate-x-1 hover:-translate-y-2 hover:translate-x-2 transition-all duration-500 ease-in-out"
            >
              Visit the Exhibit
            </button>
          </a>
        </div>
      </div>

      <div
        class="font-bold lg:text-base md:text-base mt-8 lg:mt-0 md:mt-0 text-xs text-left text-white md:max-w-[25vw] lg:max-w-[25vw] flex flex-col gap-4"
      >
        Union Zindabad traces South Asian labor history in Canada through a
        variety of lenses. Beginning with the migrations of the early twentieth
        century, this book includes chapters on early migrants, revolutionaries,
        unions, and the struggles of South Asian labor activists and leaders.
      </div>
    </div>

    <div class="h-full max-w-[50vw]">
      <div
        class="relative h-fit hidden lg:block md:block rounded-[20px] object-cover"
      >
        <img src="/cover_right.png" alt="" class="w-full" />
        <p
          hidden
          class="absolute text-[#f5f5f5] text-right text-xs font-bold bottom-4 right-4 max-w-[70%]"
        >
          On March 20, 1943 District union official Nigel Morgan reported that
          the 'East Indians' at the Youbou Mill were 100% unionized. Kaatza
          Station Museum & Archives, N01603, IWA Local 1-80, Wilmer Gold Photo
          Collection, ©United Steelworkers Local 1-1937.
        </p>
      </div>

      <div
        class="flex w-full justify-evenly lg:pt-14 md:pt-14 py-8 items-center h-full"
      >
        {#each logos as logo}
          <a href={logo.link} target="_blank">
            <img
              src={logo.image}
              alt={logo.name}
              class="lg:w-[10vw] md:w-[10vw] w-[25vw] h-auto object-contain"
            />
          </a>
        {/each}
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
