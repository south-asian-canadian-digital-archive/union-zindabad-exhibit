<script lang="ts">
  export let text: string;
  export let focus: boolean = false;

  let tooltip: HTMLElement;

  $: if (tooltip && focus) {
    tooltip.focus();
  } else if (tooltip) {
    tooltip.blur();
  }
</script>

<div class="tooltip" class:hover={focus} bind:this={tooltip}>
  <slot />

  <span class="tooltiptext py-1">{text}</span>
</div>

<style>
  .tooltip {
    position: relative;
    display: inline-block;
  }

  .tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: #555;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: opacity 0.3s;
  }

  .tooltip .tooltiptext::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #555 transparent transparent transparent;
  }

  .tooltip:hover .tooltiptext,
  .tooltip.hover .tooltiptext {
    visibility: visible;
    opacity: 1;
  }
</style>
